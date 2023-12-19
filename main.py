import shutil
def delete_directory(path):
        shutil.rmtree(path)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")