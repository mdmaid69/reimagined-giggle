  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import shutil
def move_file(src, dst):
        shutil.move(src, dst)