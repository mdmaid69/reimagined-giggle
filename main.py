import logging
def log_message(message):
        logging.info(message)
import array
def get_array_as_memoryview(array):
        return memoryview(array)