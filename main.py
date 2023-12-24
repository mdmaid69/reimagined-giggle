  import os
  def split_path(path):
        return os.path.split(path)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)