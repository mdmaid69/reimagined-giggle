  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
def convert_to_octal(n):
        return oct(n)