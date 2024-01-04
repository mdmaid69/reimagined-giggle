  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import shutil
def delete_directory(path):
        shutil.rmtree(path)