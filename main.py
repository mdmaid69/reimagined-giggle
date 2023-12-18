import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)