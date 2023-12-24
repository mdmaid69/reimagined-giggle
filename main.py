  import os
  def get_current_working_directory():
        return os.getcwd()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)