  import os
  def delete_file(file_name):
        os.remove(file_name)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)