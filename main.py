  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def is_even(n):
        return n % 2 == 0