import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)