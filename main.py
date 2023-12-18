import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")