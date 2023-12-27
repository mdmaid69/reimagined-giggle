  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)