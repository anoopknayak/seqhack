from app.helpers.util import validate_email


def validate_login_params(params):
    email = validate_email(params.get('email', None))
    password = params.get('password', None)
    return True if email and password is not None else False


def validate_signup_params(params):
    email = validate_email(params.get('email', None))
    password = params.get('password', None)
    name = params.get('name', None)
    return email and password is not None and name is not None
