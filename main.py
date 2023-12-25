import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)