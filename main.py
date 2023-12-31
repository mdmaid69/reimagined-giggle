  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")