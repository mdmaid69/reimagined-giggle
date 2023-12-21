import time
def get_current_time():
        return time.ctime()
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)