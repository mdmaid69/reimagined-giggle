  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
from collections import Counter
print(Counter("hello world"))