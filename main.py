  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)