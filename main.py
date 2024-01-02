import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)