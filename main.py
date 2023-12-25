  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  def convert_to_octal(n):
        return oct(n)