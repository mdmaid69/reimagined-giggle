  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import random
print(random.randint(0, 100))