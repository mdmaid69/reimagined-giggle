  def convert_to_hex(n):
        return hex(n)
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink