  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime