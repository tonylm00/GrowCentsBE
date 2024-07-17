import yfinance as yf
from app.Config import Asset


def get_company_from_ticker(ticker):
    return yf.Ticker(ticker).info['shortName']


def get_asset_class_from_ticker(ticker):
    if ticker in Asset.STOCKS:
        return 'Stocks'
    else:
        if ticker in Asset.ETFS:
            return 'ETFs'
        else:
            if ticker in Asset.BONDS:
                return 'Bonds'
    return 'Other'
