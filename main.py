  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)