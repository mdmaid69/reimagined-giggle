  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)