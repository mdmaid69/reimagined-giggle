  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
def reverse_string(s):
        return s[::-1]