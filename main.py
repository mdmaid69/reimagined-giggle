import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")