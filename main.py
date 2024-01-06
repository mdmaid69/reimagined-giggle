  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  def convert_to_octal(n):
        return oct(n)