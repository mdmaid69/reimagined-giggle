  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import time
def get_time_since_epoch():
        return time.time()