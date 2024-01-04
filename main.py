  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  def convert_to_binary(n):
        return bin(n)