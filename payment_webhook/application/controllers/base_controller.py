from abc import ABC
from typing import TypeVar

from flask import jsonify, request

JsonSerializable = TypeVar(
    'JsonSerializable', str, int, float, bool, list, dict, None
)


class BaseController(ABC):
    def handle(self):
        if request.method == 'GET':
            return self.get()
        elif request.method == 'POST':
            return self.post()
        elif request.method == 'PUT':
            return self.put()
        elif request.method == 'DELETE':
            return self.delete()

    @staticmethod
    def _formating_json_response(status: int, result: JsonSerializable):
        return jsonify(result), status

    def get(self):
        return self._formating_json_response(200, {'message': 'success'})

    def post(self):
        return self._formating_json_response(200, {'message': 'success'})

    def put(self):
        return self._formating_json_response(200, {'message': 'success'})

    def delete(self):
        return self._formating_json_response(200, {'message': 'success'})
