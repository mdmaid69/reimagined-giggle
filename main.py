  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import time
def get_current_time():
        return time.ctime()