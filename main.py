  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import time
def get_current_time():
        return time.ctime()