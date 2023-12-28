  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import random
print(random.randint(0, 100))