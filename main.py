  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
from collections import Counter
print(Counter("hello world"))