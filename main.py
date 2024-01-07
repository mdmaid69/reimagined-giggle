  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
def reverse_string(s):
        return s[::-1]