from flask import Flask, jsonify, request
from flask_accept import accept_fallback
import logging
from logging.config import fileConfig

fileConfig('app_logging.cfg', disable_existing_loggers=True)
app = Flask(__name__)


def log_msg(hdr):
    # Disable default
    log = logging.getLogger('werkzeug')
    log.disabled = True
    url = request.url
    method = request.method
    # Get the logger specified in the file
    logger = logging.getLogger('AppLogger')
    logger.debug(f"Received {method} request from {url} {hdr} Accept Header")


@app.route('/', methods=['GET', 'POST'])
@accept_fallback
def hello_world():
    log_msg(hdr="with out")
    return "<p>Hello, World</p>"


@hello_world.support('application/json')
def hello_world_json():
    log_msg(hdr="with")
    return jsonify(message="Hello, World")


if __name__ == '__main__':
    app.run(host='localhost')
