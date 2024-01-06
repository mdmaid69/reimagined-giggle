  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
from collections import Counter
print(Counter("hello world"))