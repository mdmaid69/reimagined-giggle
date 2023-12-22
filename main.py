  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"