  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)