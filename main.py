  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)