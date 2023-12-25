import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def split_path(path):
        return os.path.split(path)