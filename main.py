import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)