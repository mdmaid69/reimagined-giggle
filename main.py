  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")