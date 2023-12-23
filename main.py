  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import time
def get_time_since_epoch():
        return time.time()