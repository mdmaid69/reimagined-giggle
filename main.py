import time
def get_current_time():
        return time.ctime()
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)