import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)