import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime