import os
from flask import Flask
from decouple import config

from .webhooks import webhook

def create_app():
    """ Create, configure and return the Flask application """

    app = Flask(__name__)
    app.config['GITHUB_SECRET'] = config('GITHUB_SECRET')
    app.register_blueprint(webhook)

    return app