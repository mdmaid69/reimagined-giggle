import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def split_path(path):
        return os.path.split(path)