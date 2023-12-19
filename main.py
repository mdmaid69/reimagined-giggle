  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
from collections import Counter
print(Counter("hello world"))