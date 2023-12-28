  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)