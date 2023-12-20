import time
def get_current_time():
        return time.ctime()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)