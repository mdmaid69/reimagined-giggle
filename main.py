  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import shutil
def delete_directory(path):
        shutil.rmtree(path)