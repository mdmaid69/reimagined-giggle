  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
from collections import Counter
print(Counter("hello world"))