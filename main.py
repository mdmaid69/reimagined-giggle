  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)