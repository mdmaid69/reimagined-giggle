  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def convert_to_binary(n):
        return bin(n)