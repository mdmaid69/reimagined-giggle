  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
  def convert_to_hex(n):
        return hex(n)