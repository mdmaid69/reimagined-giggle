  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def convert_to_hex(n):
        return hex(n)