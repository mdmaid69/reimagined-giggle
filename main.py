  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import random
print(random.randint(0, 100))