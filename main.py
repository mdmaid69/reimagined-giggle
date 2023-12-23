  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
x = 10
y = 20
print("Sum:", x + y)