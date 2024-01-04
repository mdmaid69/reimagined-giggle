import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import array
def convert_array_to_bytes(array):
        return array.tobytes()