  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())