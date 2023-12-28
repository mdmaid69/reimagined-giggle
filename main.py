  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import shutil
def move_file(src, dst):
        shutil.move(src, dst)