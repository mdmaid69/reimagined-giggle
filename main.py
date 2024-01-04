  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import time
def get_current_time():
        return time.ctime()