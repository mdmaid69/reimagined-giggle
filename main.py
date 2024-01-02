import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode