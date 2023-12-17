import logging
def log_message(message):
        logging.info(message)
import os
def get_environment_variable(var):
        return os.getenv(var)