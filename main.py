  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import shutil
def delete_directory(path):
        shutil.rmtree(path)