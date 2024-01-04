import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)