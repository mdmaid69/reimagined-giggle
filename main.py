  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
print([x**2 for x in range(10)])