from flask_restful import Api
from app import flaskAppInstance
from .Task import Task
from .TaskBYID import TaskBYID
from .Home import Home

restServer = Api(flaskAppInstance)

restServer.add_resource(Home, "/")
restServer.add_resource(Task, "/api/task")
restServer.add_resource(TaskBYID, "/api/task/id/<string:taskID>")
