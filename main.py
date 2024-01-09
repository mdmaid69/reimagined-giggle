  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def convert_to_hex(n):
        return hex(n)