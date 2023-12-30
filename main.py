  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
def reverse_string(s):
        return s[::-1]