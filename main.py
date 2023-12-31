import logging
def log_message(message):
        logging.info(message)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)