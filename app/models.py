from . import db


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, title, content):
        self.title = title
        self.content = content


class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(4), nullable=False)
    company = db.Column(db.Text, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, ticker, unit_price, quantity, date):
        self.ticker = ticker
        self.unit_price = unit_price
        self.quantity = quantity
        self.company = self.get_company_from_ticker()
        self.date = date

    def get_company_from_ticker(self):
        import yfinance as yf
        return yf.Ticker(self.ticker).info['shortName']
