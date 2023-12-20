import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)