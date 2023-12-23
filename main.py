  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def convert_to_octal(n):
        return oct(n)