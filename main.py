import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import array
def get_array_buffer_info(array):
        return array.buffer_info()