  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
def convert_to_octal(n):
        return oct(n)