  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
def convert_to_binary(n):
        return bin(n)