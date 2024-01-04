  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
def convert_to_binary(n):
        return bin(n)