from flask import jsonify


def generate_error_response(status_code, message=None):
    message = message if message is None else "Some error occurred"
    response = jsonify(success=false, message=message)
    response.status_code = status_code
    return response


def generate_custom_response(status_code, obj):
    response = jsonify(**obj)
    response.status_code = status_code
    return response
