import time
def get_time_since_epoch():
        return time.time()
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)