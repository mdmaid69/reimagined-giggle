  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)