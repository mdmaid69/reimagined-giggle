  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import shutil
def delete_directory(path):
        shutil.rmtree(path)