import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import logging
def setup_logging(level):
        logging.basicConfig(level=level)