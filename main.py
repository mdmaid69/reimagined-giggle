  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")