from functools import wraps
from flask_parameter_validation import ValidateParameters, Json, Route, Query
from backend.composables.response import response


def __parameter_validation_error(err):
    return response.bad_request(str(err), None, "parameter_error")


# usage same as @ValidateParameters(), but applies custom error function automatically.
# can still pass override function through decorator as normal e.g. @validate_parameters(func)
def validate_parameters(error_func=__parameter_validation_error):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        # Apply the validate_parameters decorator with the custom error function
        decorated_wrapper = ValidateParameters(error_func)(wrapper)

        return decorated_wrapper
    return decorator
