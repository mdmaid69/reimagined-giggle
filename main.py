  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
from collections import Counter
print(Counter("hello world"))