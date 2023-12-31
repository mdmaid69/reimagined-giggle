  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import time
def get_time_since_epoch():
        return time.time()