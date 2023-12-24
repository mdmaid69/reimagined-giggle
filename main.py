  import os
  def delete_file(file_name):
        os.remove(file_name)
import time
def get_current_time():
        return time.ctime()