  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)