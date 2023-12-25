  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())