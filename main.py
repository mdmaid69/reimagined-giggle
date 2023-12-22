import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}