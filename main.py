  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")