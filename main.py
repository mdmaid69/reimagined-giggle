  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
n = 10
print("Square numbers:", [x**2 for x in range(n)])