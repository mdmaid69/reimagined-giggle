  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
x = 10
y = 20
print("Sum:", x + y)