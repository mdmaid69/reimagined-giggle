  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import random
print(random.randint(0, 100))