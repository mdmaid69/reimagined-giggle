  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
def convert_to_binary(n):
        return bin(n)