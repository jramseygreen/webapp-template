from functools import wraps
from flask_jwt_extended import current_user

from backend.composables.response import response


def allows(*dec_args, **dec_kwargs):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            roles = ['default']
            if current_user and current_user.roles:
                roles = current_user.roles

            for role in roles:
                role_name = 'default'
                if role != role_name:
                    role_name = role.name

                if role_name in dec_kwargs:
                    allow_request = dec_kwargs[role_name]

                    # custom validator, don't pass boolean - but rather pass a function returning a boolean
                    if callable(dec_kwargs[role_name]):
                        # the paramaters received from flask_parameter_validation are passed to the validator
                        allow_request = dec_kwargs[role_name](*args, **kwargs)

                    if allow_request:
                        return f(*args, **kwargs)

            return response.forbidden('Additional permissions required')
        return wrapper
    return decorator


def blocks(*dec_args, **dec_kwargs):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            roles = ['default']
            if current_user and current_user.roles:
                roles = current_user.roles

            for role in roles:
                role_name = 'default'
                if role != role_name:
                    role_name = role.name

                if role_name in dec_kwargs:
                    block_request = dec_kwargs[role_name]

                    # custom validator, don't pass boolean - but rather pass a function returning a boolean
                    if callable(dec_kwargs[role_name]):
                        # the paramaters received from flask_parameter_validation are passed to the validator
                        block_request = dec_kwargs[role_name](*args, **kwargs)

                    if block_request:
                        return response.forbidden('Additional permissions required')

            return f(*args, **kwargs)
        return wrapper
    return decorator
