  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)