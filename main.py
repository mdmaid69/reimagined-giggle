import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)