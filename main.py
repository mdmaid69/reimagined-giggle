  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import time
def get_time_since_epoch():
        return time.time()