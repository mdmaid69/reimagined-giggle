  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)