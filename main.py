  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)