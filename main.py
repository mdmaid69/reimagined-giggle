import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)