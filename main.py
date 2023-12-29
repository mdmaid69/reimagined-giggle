  def convert_to_octal(n):
        return oct(n)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size