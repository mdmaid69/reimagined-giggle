import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)