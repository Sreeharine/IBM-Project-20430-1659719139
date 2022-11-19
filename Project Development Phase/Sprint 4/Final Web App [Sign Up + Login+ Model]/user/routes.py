from flask import *
from user.models import User
from app import app

@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()


@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
    return User().login()