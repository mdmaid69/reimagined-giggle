  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import shutil
def move_file(src, dst):
        shutil.move(src, dst)