import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import glob
def find_files(pattern):
        return glob.glob(pattern)