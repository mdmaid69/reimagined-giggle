  import os
  def split_path(path):
        return os.path.split(path)
import shutil
def delete_directory(path):
        shutil.rmtree(path)