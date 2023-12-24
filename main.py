  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import time
def get_time_since_epoch():
        return time.time()