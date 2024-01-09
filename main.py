import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)