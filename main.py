import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size