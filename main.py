  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import time
def get_time_since_epoch():
        return time.time()