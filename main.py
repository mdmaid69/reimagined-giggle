  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)