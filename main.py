  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import shutil
def move_file(src, dst):
        shutil.move(src, dst)