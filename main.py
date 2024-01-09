  def convert_to_octal(n):
        return oct(n)
  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns