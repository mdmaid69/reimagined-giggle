import time
def get_current_time():
        return time.time()
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink