  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def convert_to_octal(n):
        return oct(n)