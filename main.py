  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)