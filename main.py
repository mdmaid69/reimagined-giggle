  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)