from app.Config import Asset
import yfinance as yf

if __name__ == '__main__':
    for stock in Asset.STOCKS:
        try:
            print(yf.Ticker(stock).info['shortName'])
        except KeyError as e:
            print(f"{e} not found on {stock} - {yf.Ticker(stock).info}")
    print("---------------------------------------------")

    for etf in Asset.ETFS:
        try:
            print(yf.Ticker(etf).info['shortName'])
        except KeyError as e:
            print(f"{e} not found on {etf} - {yf.Ticker(etf).info}")

    print("---------------------------------------------")
    for bond in Asset.BONDS:
        try:
            print(yf.Ticker(bond).info['shortName'])
        except KeyError as e:
            print(f"{e} not found on {bond} - {yf.Ticker(bond).info}")
