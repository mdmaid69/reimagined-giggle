import os
def remove_directory(path):
        os.rmdir(path)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")