import logging
def log_message(message):
        logging.info(message)
def find_difference(list1, list2):
        return set(list1) - set(list2)