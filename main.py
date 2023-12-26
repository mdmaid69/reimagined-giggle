  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import random
print(random.randint(0, 100))