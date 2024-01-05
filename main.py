  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
from collections import Counter
print(Counter("hello world"))