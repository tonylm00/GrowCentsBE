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

    ticker_with_names = {
        "AAPL": "Apple Inc.",
        "ABBV": "AbbVie Inc.",
        "ADBE": "Adobe Inc.",
        "AGG": "iShares Core U.S. Aggregate Bon",
        "AMGN": "Amgen Inc.",
        "AMZN": "Amazon.com, Inc.",
        "BA": "Boeing Company (The)",
        "BIV": "Vanguard Intermediate-Term Bond",
        "BMY": "Bristol-Myers Squibb Company",
        "BND": "Vanguard Total Bond Market ETF",
        "BNDX": "Vanguard Total International Bo",
        "BSV": "Vanguard Short-Term Bond ETF",
        "CAT": "Caterpillar, Inc.",
        "CMCSA": "Comcast Corporation",
        "COST": "Costco Wholesale Corporation",
        "CRM": "Salesforce, Inc.",
        "CSCO": "Cisco Systems, Inc.",
        "CVX": "Chevron Corporation",
        "DHR": "Danaher Corporation",
        "DIA": "SPDR Dow Jones Industrial Avera",
        "DIS": "Walt Disney Company (The)",
        "GOOG": "Alphabet Inc.",
        "HD": "Home Depot, Inc. (The)",
        "HON": "Honeywell International Inc.",
        "HYG": "iShares iBoxx $ High Yield Corp",
        "IBM": "International Business Machines",
        "IEF": "iShares 7-10 Year Treasury Bond",
        "INTC": "Intel Corporation",
        "IVV": "iShares Core S&P 500 ETF",
        "IWM": "iShares Russell 2000 ETF",
        "JNJ": "Johnson & Johnson",
        "JPM": "JP Morgan Chase & Co.",
        "KO": "Coca-Cola Company (The)",
        "LLY": "Eli Lilly and Company",
        "LQD": "iShares iBoxx $ Investment Grad",
        "MA": "Mastercard Incorporated",
        "MCD": "McDonald's Corporation",
        "MDT": "Medtronic plc.",
        "MMM": "3M Company",
        "MRK": "Merck & Company, Inc.",
        "MSFT": "Microsoft Corporation",
        "NEE": "NextEra Energy, Inc.",
        "NKE": "Nike, Inc.",
        "NVDA": "NVIDIA Corporation",
        "ORCL": "Oracle Corporation",
        "PEP": "Pepsico, Inc.",
        "PFE": "Pfizer, Inc.",
        "PG": "Procter & Gamble Company (The)",
        "QCOM": "QUALCOMM Incorporated",
        "QQQ": "Invesco QQQ Trust, Series 1",
        "SHY": "iShares 1-3 Year Treasury Bond ",
        "SPY": "SPDR S&P 500",
        "T": "AT&T Inc.",
        "TIP": "iShares TIPS Bond ETF",
        "TIPS": "Tianrong Internet Products and ",
        "TLT": "iShares 20+ Year Treasury Bond ",
        "TSLA": "Tesla, Inc.",
        "TXN": "Texas Instruments Incorporated",
        "UNH": "UnitedHealth Group Incorporated",
        "UPS": "United Parcel Service, Inc.",
        "V": "Visa Inc.",
        "VCIT": "Vanguard Intermediate-Term Corp",
        "VEA": "Vanguard FTSE Developed Markets",
        "VIG": "Vanguard Div Appreciation ETF",
        "VNQ": "Vanguard Real Estate ETF",
        "VOO": "Vanguard S&P 500 ETF",
        "VTI": "Vanguard Total Stock Market ETF",
        "VWO": "Vanguard FTSE Emerging Markets ",
        "VZ": "Verizon Communications Inc.",
        "WFC": "Wells Fargo & Company",
        "WMT": "Walmart Inc.",
        "XLE": "SPDR Select Sector Fund - Energ",
        "XLF": "SPDR Select Sector Fund - Finan",
        "XLI": "SPDR Select Sector Fund - Indus",
        "XLK": "SPDR Select Sector Fund - Techn",
        "XLV": "SPDR Select Sector Fund - Healt",
        "XOM": "Exxon Mobil Corporation"
    }
