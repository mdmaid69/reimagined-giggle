  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
from collections import Counter
print(Counter("hello world"))