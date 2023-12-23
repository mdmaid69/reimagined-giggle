  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import time
def get_time_since_epoch():
        return time.time()