import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)