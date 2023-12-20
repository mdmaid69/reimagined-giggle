  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)