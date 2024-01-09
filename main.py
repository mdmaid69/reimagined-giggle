  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")