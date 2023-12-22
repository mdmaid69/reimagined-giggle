import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array