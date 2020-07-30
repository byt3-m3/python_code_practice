import logging
from functools import wraps


def debug(msg):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.debug(msg)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def critical(msg):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.critical(msg)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def info(msg):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(msg)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def error(msg):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.error(msg)
            return func(*args, **kwargs)

        return wrapper

    return decorator
