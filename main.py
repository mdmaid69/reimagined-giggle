  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])