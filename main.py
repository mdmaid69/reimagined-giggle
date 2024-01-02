  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import time
def get_time_since_epoch():
        return time.time()