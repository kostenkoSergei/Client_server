import logging

# log format: "<date-time> <level> <module_name> <message>"
_log_format = f'%(asctime)s - %(levelname)s - %(module)s - %(message)s '
# create formatter object
formatter = logging.Formatter(_log_format)

# create file handler (encoding is optional)
# logging has to be done to a log file
file_handler = logging.FileHandler('log/client.main.log', encoding='utf-8')
# file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# create named logging class instance
client_logger = logging.getLogger('client.main')

# add new handler to a logger and set level of logging to debug
client_logger.addHandler(file_handler)
client_logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # test
    client_logger.info('logging test')
    client_logger.warning('logging test')

    # level of logging
    client_logger.setLevel(logging.WARNING)

    # test
    client_logger.debug('logging test')
    client_logger.critical('logging test')
