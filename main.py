import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def find_common_elements(list1, list2):
        return set(list1) & set(list2)