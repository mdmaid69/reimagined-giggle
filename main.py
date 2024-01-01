def convert_to_hex(n):
        return hex(n)
  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev