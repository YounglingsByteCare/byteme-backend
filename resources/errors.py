from flask_restful import HTTPException

class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class ItemAlreadyExistsError(HTTPException):
    pass

class UpdatingItemError(Exception):
    pass

class DeletingItemError(Exception):
    pass

class ItemNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

class EmailDoesnotExistsError(Exception):
    pass

class BadTokenError(Exception):
    pass

errors = {
    "InternalServerError": {
        "type": "InternalServerError",
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "type": "SchemaValidationError",
         "message": "Request is missing required fields",
         "status": 400
     },
     "ItemAlreadyExistsError": {
         "type": "ItemAlreadyExistsError",
         "message": "Item with given name already exists",
         "status": 400
     },
     "UpdatingItemError": {
         "type": "UpdatingItemError",
         "message": "Updating item added by other is forbidden",
         "status": 403
     },
     "DeletingItemError": {
         "type": "DeletingItemError",
         "message": "Deleting item added by other is forbidden",
         "status": 403
     },
     "ItemNotExistsError": {
         "type": "ItemNotExistsError",
         "message": "Item with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "type": "EmailAlreadyExistsError",
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "type": "UnauthorizedError",
         "message": "Invalid username or password",
         "status": 401
     },
     "EmailDoesnotExistsError": {
         "type": "EmailDoesnotExistsError",
         "message": "Couldn't find the user with given email address",
          "status": 400
     },
     "BadTokenError": {
         "type": "BadTokenError",
         "message": "Invalid token",
         "status": 403
     }
}
