  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
from collections import Counter
print(Counter("hello world"))