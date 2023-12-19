  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import time
def get_time_since_epoch():
        return time.time()