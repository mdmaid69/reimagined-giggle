  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)