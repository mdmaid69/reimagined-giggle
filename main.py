  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  def convert_to_binary(n):
        return bin(n)