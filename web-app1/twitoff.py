"""Main app/routing file for TwitOff!"""
#import flask
from flask import Flask, render_template
from .models import DB, insert_example_users, User
def create_app():
  app = Flask(__name__)
  
  app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///db.sqlite3'
  #app.config["ENV"] = config("ENV")
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  DB.init_app(app)
  @app.route('/')
  def root():
    DB.drop_all()
    DB.create_all()
    insert_example_users()
    users = User.query.all()
    return render_template('base.html', title="home", users=User.query.all())
  #@app.route('/user')
  #def root_user(): 
  return app
