import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import logging
def log_message(message):
        logging.info(message)