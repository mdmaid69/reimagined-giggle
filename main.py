  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
from collections import Counter
print(Counter("hello world"))