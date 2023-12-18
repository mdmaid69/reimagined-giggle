  import os
  def delete_file(file_name):
        os.remove(file_name)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)