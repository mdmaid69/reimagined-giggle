import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)