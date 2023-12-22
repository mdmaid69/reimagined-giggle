import os
def remove_directory(path):
        os.rmdir(path)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)