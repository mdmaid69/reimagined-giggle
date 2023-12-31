  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
  def convert_to_octal(n):
        return oct(n)