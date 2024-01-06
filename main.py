  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")