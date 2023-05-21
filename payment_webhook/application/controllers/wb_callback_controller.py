import json

from flask import request
from werkzeug.exceptions import UnsupportedMediaType

from ..payment_handle import PaymentHandle
from .base_controller import BaseController


class WebHookCallbackController(BaseController):
    def get(self):
        return self._formating_json_response(
            status=405, result={'message': 'Method not allowed'}
        )

    def post(self):
        if not request.data:
            return self._formating_json_response(
                status=400, result={'message': 'Necessary Payment data'}
            )
        try:
            body = request.get_json()
        except UnsupportedMediaType as er:
            body = json.loads(request.data.decode('utf-8'))
        handle = PaymentHandle()
        try:
            status = handle.process(body=body)
            result = {
                'message': 'Success Webhook storage',
                'paymentStatus': status.value,
            }
            return self._formating_json_response(status=200, result=result)
        except Exception as er:
            return self._formating_json_response(
                status=500,
                result={'message': f'Unspected error. Detail: {er}'},
            )
