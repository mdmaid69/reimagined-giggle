  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
  def convert_to_octal(n):
        return oct(n)