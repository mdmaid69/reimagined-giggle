  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
from collections import Counter
print(Counter("hello world"))