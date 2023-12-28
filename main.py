import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)