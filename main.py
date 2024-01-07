import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)