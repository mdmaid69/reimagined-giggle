import logging
def log_message(message):
        logging.info(message)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)