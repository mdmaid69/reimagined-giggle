import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import array
def insert_into_array(array, i, item):
        array.insert(i, item)