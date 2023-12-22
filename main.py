  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size