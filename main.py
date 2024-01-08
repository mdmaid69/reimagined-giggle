  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
from collections import Counter
print(Counter("hello world"))