  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def reverse_string(s):
        return s[::-1]