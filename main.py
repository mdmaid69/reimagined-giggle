  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")