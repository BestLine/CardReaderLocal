import logging

logging.basicConfig(format='%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG, filename='error_log.log')

def debug_message(error):
    logging.debug(error)

def info_message(error):
    logging.info(error)

def warning_message(error):
    logging.warning(error)

def error_message(error):
    logging.error(error)

def critical_message(error):
    logging.critical(error)
