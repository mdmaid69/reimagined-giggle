import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import array
def extend_array(array, iterable):
        array.extend(iterable)