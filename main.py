n = 10
print("Cube numbers:", [x**3 for x in range(n)])
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize