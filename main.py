def convert_to_octal(n):
        return oct(n)
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino