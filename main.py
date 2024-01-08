  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)