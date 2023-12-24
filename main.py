  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import time
def get_time_since_epoch():
        return time.time()