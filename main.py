import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]