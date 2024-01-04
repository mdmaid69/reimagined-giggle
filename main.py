  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  def reverse_list(lst):
        return lst[::-1]