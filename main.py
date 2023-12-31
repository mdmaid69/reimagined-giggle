  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
from collections import Counter
print(Counter("hello world"))