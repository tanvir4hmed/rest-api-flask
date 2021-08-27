from flask import Flask, request, app
import logging as logger

logger.basicConfig(level="DEBUG")

# init app
flaskAppInstance = Flask(__name__)


# @flaskAppInstance.route("/", methods=['GET'])
# def home():
#     return "Hello World"


if __name__ == '__main__':
    logger.debug('Starting The Application')
    from api import *
    flaskAppInstance.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
