import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import os
  def split_path(path):
        return os.path.split(path)