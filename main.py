import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)