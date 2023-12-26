  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)