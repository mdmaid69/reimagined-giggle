  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import time
def get_time_since_epoch():
        return time.time()