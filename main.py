import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")