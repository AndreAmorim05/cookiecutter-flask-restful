from flask import request
from flask_restful import Resource

__all__ = ("ApiArea",)


class ApiArea(Resource):
    def get(self, id):
        return "Api Area"

    def post(self):
        args = request.get_json(force=True)
        print(args)
        return 201

    def put(self, id):
        ...

    def delete(self, id):
        ...
