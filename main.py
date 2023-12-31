  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import shutil
def delete_directory(path):
        shutil.rmtree(path)