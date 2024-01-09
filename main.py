import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import os
def list_files_in_directory(path):
        return os.listdir(path)