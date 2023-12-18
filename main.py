  import os
  def get_current_directory():
        return os.getcwd()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)