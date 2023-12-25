  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
from collections import Counter
print(Counter("hello world"))