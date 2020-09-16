"""Main app/routing file for TwitOff!"""
#import the flask
from flask import Flask, render_template, request
from .models import DB, insert_example_users, User
from .twitter import add_or_update_user
from os import getenv

# create function for the app
def create_app():
    app = Flask(__name__)

    #for storing information in our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    #app.config["ENV"] = ("ENV")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)
    @app.route('/')

    def root():
        DB.drop_all()
        DB.create_all()
        insert_example_users()
        users = User.query.all()
        return render_template('base.html', title="home", users=User.query.all())

    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        name = name if name else request.values['user_name']
        try:
            if request.method =='POST':
                add_or_update_user(name)
                message = "User {} successfully added!".format(name)
            tweets = User.query.filter(User.name == name).one().tweets
        except Exception as e:
            message = "Error addding {}: {}".format(name, e)
            tweets=[]
        return render_template('user.html', title=name, tweets=tweets, message=message)

    #associated with update button
    @app.route('/update')
    def update():
        insert_example_users()
        return render_template('base.html', title="users updated!", users=User.query.all()) 

    #associated with reset button       
    @app.route("/reset")
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title="Reset Database")
    return app