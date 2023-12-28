  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
from collections import Counter
print(Counter("hello world"))