import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]