import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev