  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import time
def get_time_since_epoch():
        return time.time()