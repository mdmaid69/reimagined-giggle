import time
def get_current_time():
        return time.ctime()
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino