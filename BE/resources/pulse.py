from flask_restful import Resource, request
from services import DBService
from http import HTTPStatus


db_service = DBService()

class Pulse(Resource):
    
    def get(self):
        try:
            pulses = db_service.get_pulses()
            return {'pulses': pulses}, HTTPStatus.OK
        except Exception as e:
            return {'error': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def post(self):
        try:
            pulse = request.get_json()
            pulse_id = db_service.create_pulse(pulse)
            return {'pulse_id': pulse_id}, HTTPStatus.CREATED
        except Exception as e:
            return {'error': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def put(self):
        try:
            pulse = request.get_json()
            pulse_id = db_service.update_pulse(pulse)
            return {'pulse_id': pulse_id}, HTTPStatus.CREATED
        except Exception as e:
            return {'error': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR