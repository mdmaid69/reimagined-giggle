  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def convert_to_binary(n):
        return bin(n)