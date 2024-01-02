  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
n = 10
print("Square numbers:", [x**2 for x in range(n)])