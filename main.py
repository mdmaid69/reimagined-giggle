  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())