import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import os
def get_file_size(filename):
        return os.path.getsize(filename)