  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  def convert_to_hex(n):
        return hex(n)