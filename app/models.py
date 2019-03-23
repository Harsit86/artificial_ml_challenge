from app.db import db


class CustomerDetails(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.Unicode(100), nullable=False)
    marital = db.Column(db.Unicode(50), nullable=False)
    education = db.Column(db.Unicode(50), nullable=False)
    default = db.Column(db.Unicode(10), nullable=False)
    balance = db.Column(db.BigInteger, nullable=False)
    housing = db.Column(db.Unicode(10), nullable=False)
    loan = db.Column(db.Unicode(10), nullable=False)
    contact = db.Column(db.Unicode(10), nullable=False)
    day = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Unicode(10), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    campaign = db.Column(db.Integer, nullable=False)
    pdays = db.Column(db.Integer, nullable=False)
    previous = db.Column(db.Integer, nullable=False)
    poutcome = db.Column(db.Unicode(10), nullable=False)
    y = db.Column(db.Unicode(5), nullable=False)
