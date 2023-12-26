  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
for i in range(10): print(i)