import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import array
def get_string_from_array(array):
        return array.tobytes()