import random
print(random.randint(0, 100))
  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags