import traceback
from functools import wraps
import logging
import inspect


def check_logging_level(logging_level):
    logging_levels = {
        'CRITICAL': 'critical',
        'ERROR': 'error',
        'WARNING': 'warning',
        'INFO': 'info',
        'DEBUG': 'debug',
        'NOTSET': 'notset',
    }
    if logging_level in logging_levels:
        return logging_levels[logging_level]
    raise ValueError


def get_decorator_logger():
    _log_format = f'%(asctime)s - %(message)s'
    formatter = logging.Formatter(_log_format)
    file_handler = logging.FileHandler("log/logger_decorator.log", encoding='utf-8')
    file_handler.setFormatter(formatter)
    log_decorator_logger = logging.getLogger('logger_decorator')
    log_decorator_logger.addHandler(file_handler)
    log_decorator_logger.setLevel(logging.DEBUG)
    return log_decorator_logger


"""
inspect.stack(context=1)
Return a list of frame records for the caller’s stack. The first entry in the returned list represents the caller; the 
last entry represents the outermost call on the stack.
Changed in version 3.5: A list of named tuples FrameInfo(frame, filename, lineno, function, code_context, index) 
is returned.
"""


def log():
    """function based logger decorator"""

    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            get_decorator_logger().info(
                f'Function "{func.__name__}" was called from function "{inspect.stack()[1][3]}".'
            )

            res = func(*args, **kwargs)
            return res

        return decorated

    return decorator


class Log():
    """class based logger decorator"""

    def __init__(self, logging_level):
        self.logging_level = logging_level

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            print(check_logging_level(self.logging_level))
            get_decorator_logger().info(
                f'Function "{func.__name__}" was called from function "{inspect.stack()[1][3]}".'
            )
            # decorated function
            res = func(*args, **kwargs)
            return res

        return decorated
