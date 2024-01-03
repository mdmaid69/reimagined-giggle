  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
  def convert_to_binary(n):
        return bin(n)