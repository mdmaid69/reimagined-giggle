import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import array
def get_bytes_from_array(array):
        return array.tobytes()