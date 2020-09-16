
"""SQLALchemy models for Twitoff"""
from os import getenv
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()
class User(DB.Model):
    """Twitter users that we pull and analyze"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return '<User {}>'.format(self.name)
class Tweet(DB.Model):
    """Tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    embedding = DB.Column(DB.PickleType, nullable = False) 
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
    def __repr__(self):
        return '<Tweet {}>'.format(self.text)
def insert_example_users():
    osm = User(id=1, name='Osman')
    mal = User(id=2, name='Malaz')
    mo = User(id=3, name='Mohamed')
    elon = User(id=4, name='elonmusk')
    ah = User(id=5, name='Ahmed')
    sa = User(id=6, name='Sara')
    ad = User(id=7, name='Adam')
    so = User(id=8, name='Sonyia')
    ra = User(id=9, name='Rowan')
    rh = User(id=10, name='rrherr')
    DB.session.add(osm)
    DB.session.add(mal)
    DB.session.add(mo)
    DB.session.add(elon)
    DB.session.add(ah)
    DB.session.add(sa)
    DB.session.add(ad)
    DB.session.add(so)
    DB.session.add(ra)
    DB.session.add(rh)
    DB.session.commit()