  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")