import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)