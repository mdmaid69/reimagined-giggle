  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
def is_odd(n):
        return n % 2 != 0