import logging

import requests

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def launch():
	msg = render_template('welcome')
	return question(msg)

@ask.intent("FlipIntent")

def flip():
	requests.get('https://alexa-blackjack-gk.herokuapp.com/flip')
	msg = render_template('flip')
	return statement(msg)


if __name__ == '__main__':

    app.run(debug=True)