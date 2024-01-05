import os
def change_working_directory(path):
        os.chdir(path)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)