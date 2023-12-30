  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import random
print(random.randint(0, 100))