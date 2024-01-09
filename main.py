def convert_to_binary(n):
        return bin(n)
  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime