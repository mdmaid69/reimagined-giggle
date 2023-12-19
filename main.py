  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import shutil
def delete_directory(path):
        shutil.rmtree(path)