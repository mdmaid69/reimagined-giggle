  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
def convert_to_hex(n):
        return hex(n)