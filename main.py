  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
def convert_to_hex(n):
        return hex(n)