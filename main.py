  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import shutil
def move_file(src, dst):
        shutil.move(src, dst)