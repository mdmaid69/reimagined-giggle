import time
def get_time_since_epoch():
        return time.time()
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize