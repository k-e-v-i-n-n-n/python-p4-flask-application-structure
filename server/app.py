#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>You are on the app bb<h1>'

@app.route('/<string:username>')
def user(username):
    return f'This is the home of {username}'

if __name__ == '__main__':
    app.run(port=8000, debug=True)