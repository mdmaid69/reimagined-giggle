import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]