import time
def get_current_time():
        return time.ctime()
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize