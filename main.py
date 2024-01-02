  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)