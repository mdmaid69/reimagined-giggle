from collections import Counter
print(Counter("hello world"))
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino