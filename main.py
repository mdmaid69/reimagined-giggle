  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")