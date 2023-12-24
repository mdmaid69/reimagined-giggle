  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  def convert_to_hex(n):
        return hex(n)