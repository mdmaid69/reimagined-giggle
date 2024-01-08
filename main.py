import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)