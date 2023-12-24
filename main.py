import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)