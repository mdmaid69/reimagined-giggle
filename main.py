  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)