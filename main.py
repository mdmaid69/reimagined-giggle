import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)