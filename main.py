import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)