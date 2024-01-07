import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)