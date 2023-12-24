import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable