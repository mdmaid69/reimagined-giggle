  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
  def convert_to_binary(n):
        return bin(n)