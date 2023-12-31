  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")