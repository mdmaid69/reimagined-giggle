  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")