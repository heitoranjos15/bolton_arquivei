import json
import logging

from flask_api import status
from flask_restful import Resource, abort
from flask import request
from src.builders.invoice import get_invoice


class Invoice(Resource):
    def post(self):
        logger_detail = {
            'scope': 'invoice/post',
            'data_received': request.get_json(force=True)
        }
        access_key = request.get_json(force=True).get('access_key')
        if not access_key: return {'message': 'param access_key not sent'}, 400
        try:
            invoice = get_invoice(access_key)
            if not invoice:
                logging.error(
                    f'access key not found, {json.dumps(logger_detail)}')
                return {'message': 'invoice not found'}, 404
        except Exception as error:
            logging.error(
                f'Error while trying to search invoice, {json.dumps(logger_detail)}, {error}')
            return {'message': 'internal error', 'error': str(error)}, 500
        return {'xml_value': invoice}, 200
