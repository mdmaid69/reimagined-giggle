import random
print(random.randint(0, 100))
  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns