  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
def convert_to_octal(n):
        return oct(n)