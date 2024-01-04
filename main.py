  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)