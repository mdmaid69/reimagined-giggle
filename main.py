  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import time
def get_time_since_epoch():
        return time.time()