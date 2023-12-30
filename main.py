import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)