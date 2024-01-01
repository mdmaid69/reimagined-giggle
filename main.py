import logging
def log_message(message):
        logging.info(message)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)