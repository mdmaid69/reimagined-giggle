  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)