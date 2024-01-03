  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)