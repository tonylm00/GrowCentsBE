from flask import Blueprint, request, jsonify
from ..models import Trade
from ..schemas import trade_schema, trades_schema
from .. import db
import yfinance as yf
from ..Config import Asset
import logging
from datetime import datetime

bp = Blueprint('trades', __name__, url_prefix='/trades')

logger = logging.getLogger(__name__)


def get_company_name(ticker):
    try:
        return yf.Ticker(ticker).info['shortName']
    except Exception as e:
        logger.error("Error getting company name for ticker %s: %s", ticker, str(e))
        return "Unknown"


@bp.route('/', methods=['POST'])
def add_trade():
    try:
        logger.debug("Request data: %s", request.json)
        ticker = request.json['ticker']
        if ticker not in Asset.STOCKS + Asset.ETFS + Asset.BONDS:
            return jsonify({"error": "Ticker non accettato"}), 400

        unit_price = request.json['unit_price']
        quantity = request.json['quantity']
        date_str = request.json['date']
        date = datetime.fromisoformat(date_str)

        trade_item = Trade(ticker, unit_price, quantity, date)
        db.session.add(trade_item)
        db.session.commit()

        return trade_schema.jsonify(trade_item)
    except Exception as e:
        logger.error("Error adding trade: %s", str(e))
        return jsonify({"error": str(e)}), 500


@bp.route('/', methods=['GET'])
def get_trades():
    try:
        all_trades = Trade.query.all()
        result = trades_schema.dump(all_trades)
        return jsonify(result)
    except Exception as e:
        logger.error("Error getting trades: %s", str(e))
        return jsonify({"error": str(e)}), 500


@bp.route('/portfolio_value', methods=['GET'])
def get_portfolio_value():
    try:
        all_trades = Trade.query.all()
        total_value = 0.0
        for trade in all_trades:
            ticker = trade.ticker
            current_price = yf.Ticker(ticker).history(period="1d")['Close'].iloc[0]
            total_value += current_price * trade.quantity
        return jsonify({"total_value": total_value})
    except Exception as e:
        logger.error("Error calculating portfolio value: %s", str(e))
        return jsonify({"error": str(e)}), 500


@bp.route('/graph_data', methods=['GET'])
def get_graph_data():
    try:
        period = request.args.get('period', '1mo')
        valid_periods = ['1mo', '3mo', '6mo', '1y', 'max']
        if period not in valid_periods:
            return jsonify({"error": "Invalid period"}), 400

        all_trades = Trade.query.all()
        tickers = list(set([trade.ticker for trade in all_trades]))

        if not tickers:
            return jsonify([])

        data_frames = [yf.Ticker(ticker).history(period=period)['Close'] for ticker in tickers]
        combined_df = sum(data_frames) / len(data_frames)
        combined_df = combined_df.reset_index()
        combined_df['Date'] = combined_df['Date'].dt.strftime('%Y-%m-%d')

        # Rimuovi righe con valori NaN
        combined_df = combined_df.dropna(subset=['Close'])
        combined_df = combined_df.to_dict(orient='records')

        return jsonify(combined_df)
    except Exception as e:
        logger.error("Error getting graph data: %s", str(e))
        return jsonify({"error": str(e)}), 500


@bp.route('/supported_tickers', methods=['GET'])
def get_supported_tickers():
    """
    try:
        tickers = Asset.STOCKS + Asset.ETFS + Asset.BONDS
        ticker_with_names = {ticker: get_company_name(ticker) for ticker in tickers}
        return jsonify(ticker_with_names)
    except Exception as e:
        logger.error("Error getting supported tickers: %s", str(e))
        return jsonify({"error": str(e)}), 500
    """
    return Asset.ticker_with_names

@bp.route('/current_price', methods=['GET'])
def get_current_price():
    try:
        ticker = request.args.get('ticker')
        if not ticker:
            return jsonify({"error": "Ticker is required"}), 400

        current_price = yf.Ticker(ticker).history(period="1d")['Close'].iloc[0]
        return jsonify({"price": current_price})
    except Exception as e:
        logger.error("Error fetching current price for ticker %s: %s", ticker, str(e))
        return jsonify({"error": str(e)}), 500


@bp.route('/<int:id>', methods=['DELETE'])
def delete_trade(id):
    try:
        trade = Trade.query.get(id)
        if trade is None:
            return jsonify({"error": "Trade not found"}), 404
        db.session.delete(trade)
        db.session.commit()
        return jsonify({"message": "Trade deleted successfully"}), 200
    except Exception as e:
        logger.error("Error deleting trade: %s", str(e))
        return jsonify({"error": str(e)}), 500


@bp.route('/top_assets', methods=['GET'])
def get_top_assets():
    try:
        tickers = ['GOOG', 'AAPL', 'MSFT', 'AMZN', 'TSLA', 'QQQ', 'SPY', 'VWO', 'BND', 'IEF', 'TIPS']
        assets = []

        for ticker in tickers:
            company_info = yf.Ticker(ticker).info
            company_name = company_info.get('shortName', "Unknown")
            history_data = yf.Ticker(ticker).history(period="3mo")
            current_price = history_data['Close'].iloc[-1] if not history_data['Close'].empty else 0.0
            history = history_data.reset_index().to_dict(orient='records') if not history_data.empty else []

            # Formattazione delle date
            for record in history:
                record['Date'] = record['Date'].strftime('%Y-%m-%d %H:%M:%S')

            assets.append({
                'ticker': ticker,
                'company': company_name,
                'current_price': current_price,
                'history': history
            })

        return jsonify(assets)
    except Exception as e:
        logger.error("Error fetching top assets: %s", str(e))
        return jsonify({"error": str(e)}), 500


@bp.route('/asset_details/<string:ticker>', methods=['GET'])
def get_asset_details(ticker):
    period = request.args.get('period', '1mo')
    try:
        company_info = yf.Ticker(ticker).info
        company_name = company_info.get('shortName', "Unknown")
        history_data = yf.Ticker(ticker).history(period=period)  # Usa il periodo nella richiesta
        current_price = history_data['Close'].iloc[-1] if not history_data['Close'].empty else 0.0
        history = history_data.reset_index().to_dict(orient='records') if not history_data.empty else []

        # Formattazione delle date
        for record in history:
            record['Date'] = record['Date'].strftime('%Y-%m-%d %H:%M:%S')

        asset_details = {
            'ticker': ticker,
            'company': company_name,
            'current_price': current_price,
            'history': history
        }

        return jsonify(asset_details)
    except Exception as e:
        logger.error("Error fetching asset details for %s: %s", ticker, str(e))
        return jsonify({"error": str(e)}), 500

