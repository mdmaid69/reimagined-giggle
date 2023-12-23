  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
from collections import Counter
print(Counter("hello world"))