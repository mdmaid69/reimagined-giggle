import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import logging
def log_message(message):
        logging.info(message)