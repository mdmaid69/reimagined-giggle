import array
def get_array_as_memoryview(array):
        return memoryview(array)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")