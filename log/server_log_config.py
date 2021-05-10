import logging
from logging.handlers import TimedRotatingFileHandler

# log format: "<date-time> <level> <module_name> <message>"
_log_format = f'%(asctime)s - %(levelname)s - %(module)s - %(message)s '
# create formatter object
formatter = logging.Formatter(_log_format)

# create file handler (encoding is optional)
# logging has to be done to a log file
file_handler = logging.FileHandler("log/server.main.log", encoding='utf-8')
file_handler.setFormatter(formatter)

# create daily rotation of log files on server side
time_rotating_handler = TimedRotatingFileHandler("log/server.main.log", when='midnight', interval=1,
                                                 backupCount=7, encoding='utf-8')
# file_handler.setLevel(logging.DEBUG)
time_rotating_handler.setFormatter(formatter)

# create named logging class instance
server_logger = logging.getLogger('server.main')

# add new handler to a logger and set level of logging to debug
server_logger.addHandler(time_rotating_handler)
server_logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # test
    server_logger.info('logging test')
    server_logger.warning('logging test')

    # level of logging
    server_logger.setLevel(logging.WARNING)

    # test
    server_logger.debug('logging test')
    server_logger.critical('logging test')
