from flask_restful import Resource
import logging as logger


class Home(Resource):

    def get(self):
        logger.debug("Inside Home Page")
        return {"message": "Hello World you are in home"}, 200
