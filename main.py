  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]