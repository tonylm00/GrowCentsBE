import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../instance/db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Asset:
    STOCKS = [
        'GOOG', 'AAPL', 'MSFT', 'AMZN', 'TSLA', 'JPM', 'V', 'JNJ',
        'WMT', 'PG', 'MA', 'NVDA', 'HD', 'UNH', 'VZ', 'PFE', 'KO', 'INTC',
        'DIS', 'CMCSA', 'T', 'NKE', 'MRK', 'ABBV', 'XOM', 'CVX', 'WFC', 'MCD',
        'ORCL', 'IBM', 'CSCO', 'BA', 'LLY', 'CRM', 'PEP', 'ADBE', 'MDT', 'HON',
        'AMGN', 'UPS', 'CAT', 'MMM', 'TXN', 'NEE', 'QCOM', 'COST', 'DHR', 'BMY'
    ]

    ETFS = [
        'SPY', 'IVV', 'VOO', 'VTI', 'QQQ', 'IWM', 'DIA', 'VEA', 'VWO', 'VNQ',
        'VIG', 'AGG', 'BND', 'LQD', 'HYG', 'XLK', 'XLF', 'XLE', 'XLI', 'XLV'
    ]

    BONDS = [
        'TIPS', 'AGG', 'BND', 'LQD', 'HYG', 'SHY', 'IEF', 'TLT', 'TIP', 'BIV', 'BNDX', 'BSV', 'VCIT'
    ]
