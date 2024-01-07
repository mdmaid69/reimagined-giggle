import logging
def log_message(message):
        logging.info(message)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable