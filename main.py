import logging
def log_message(message):
        logging.info(message)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)