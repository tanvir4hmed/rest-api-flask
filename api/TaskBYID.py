from flask_restful import Resource
import logging as logger


class TaskBYID(Resource):

    def get(self, taskID):
        logger.debug("Inside Get Method of Task by Id")
        return {"message": "Inside Get Method of Task by ID. TASK-ID = {}".format(taskID)}, 200

    def post(self, taskID):
        logger.debug("Inside Post Method")
        return {"message": "Inside Post Method of Task by ID. TASK-ID = {}".format(taskID)}, 200

    def put(self, taskID):
        logger.debug("Inside Put Method")
        return {"message": "Inside Put Method of Task by ID. TASK-ID = {}".format(taskID)}, 200

    def delete(self, taskID):
        logger.debug("Inside Delete Method")
        return {"message": "Inside Delete Method of Task by ID. TASK-ID = {}".format(taskID)}, 200
