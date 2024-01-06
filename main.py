from collections import Counter
print(Counter("hello world"))
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)