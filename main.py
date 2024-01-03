  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")