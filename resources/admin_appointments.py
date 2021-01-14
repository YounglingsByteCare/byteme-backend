from flask import Response, request
from database.models import Appointment
from flask_restful import Resource

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

class AdminAppointmentsApi(Resource):
    def get(self):
        appointment = Appointment.objects().to_json()
        return Response(appointment, mimetype="application/json", status=200)
