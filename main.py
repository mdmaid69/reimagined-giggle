  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
def add_numbers(a, b):
        return a + b