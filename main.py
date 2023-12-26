  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import time
def get_current_time():
        return time.ctime()