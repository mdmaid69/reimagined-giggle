import logging
def log_message(message):
        logging.info(message)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)