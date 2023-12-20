  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
from collections import Counter
print(Counter("hello world"))