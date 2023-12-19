  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import time
def get_time_since_epoch():
        return time.time()