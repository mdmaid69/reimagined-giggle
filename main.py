  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)