import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)