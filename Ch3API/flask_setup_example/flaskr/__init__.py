from flask import Flask, jsonify
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return jsonify({'message': 'Hello World'})

    @app.route('/smiley')
    def smiley():
        return ':)'

    return app