import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)