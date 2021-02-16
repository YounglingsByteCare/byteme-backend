import sys
from flask import Response, request, jsonify
from database.models import Patient, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, ItemAlreadyExistsError, \
InternalServerError, UpdatingItemError, DeletingItemError, ItemNotExistsError

class UserApi(Resource):
    @jwt_required
    def get(self):
        try:
	        user_id = get_jwt_identity()
	        user = User.objects.get(id=user_id)
	        user_data = {
                'email': user.email,
                'patients': user.patients,
                'appointments': user.appointments
	        }
	        return jsonify(user_data)
        except DoesNotExist:
            raise ItemNotExistsError
        except Exception:
            raise InternalServerError

