import time
def get_current_time():
        return time.ctime()
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime