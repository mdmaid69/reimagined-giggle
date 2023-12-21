  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
from collections import Counter
print(Counter("hello world"))