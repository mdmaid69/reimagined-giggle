  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import time
def get_time_since_epoch():
        return time.time()