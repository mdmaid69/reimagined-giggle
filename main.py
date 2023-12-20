  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import random
print(random.randint(0, 100))