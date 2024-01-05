  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
  def convert_to_hex(n):
        return hex(n)