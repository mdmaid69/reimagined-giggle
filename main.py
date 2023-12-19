import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)