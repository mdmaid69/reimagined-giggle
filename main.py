  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def reverse_string(s):
        return s[::-1]