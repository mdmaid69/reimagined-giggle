import os
def change_working_directory(path):
        os.chdir(path)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")