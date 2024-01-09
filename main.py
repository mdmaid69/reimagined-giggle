  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
def convert_to_hex(n):
        return hex(n)