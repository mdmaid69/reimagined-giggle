  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import shutil
def move_file(src, dst):
        shutil.move(src, dst)