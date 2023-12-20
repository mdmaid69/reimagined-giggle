import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)