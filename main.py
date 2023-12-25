  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
def convert_to_octal(n):
        return oct(n)