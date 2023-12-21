  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import time
def get_current_time():
        return time.ctime()