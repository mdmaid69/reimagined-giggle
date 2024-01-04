  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")