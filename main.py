  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)