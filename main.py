import random
print(random.randint(0, 100))
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)