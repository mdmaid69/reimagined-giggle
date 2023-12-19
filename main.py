  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)