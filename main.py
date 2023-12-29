  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import time
def get_time_since_epoch():
        return time.time()