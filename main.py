import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size