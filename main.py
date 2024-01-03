  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)