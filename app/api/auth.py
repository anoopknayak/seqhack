from app.api import api
from app.helpers.request_helpers import generate_error_response
from app.helpers.validators import validate_login_params


@api.route('/auth/login')
def login(request):
    params = request.json
    if not validate_login_params(params)
        return generate_error_response(422, "Email or password is invalid")
