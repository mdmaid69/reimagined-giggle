import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev