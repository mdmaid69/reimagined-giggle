  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def calculate_average(lst):
        return sum(lst) / len(lst)