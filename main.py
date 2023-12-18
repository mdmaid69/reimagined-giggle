  import os
  def split_path(path):
        return os.path.split(path)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)