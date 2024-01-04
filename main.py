  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
n = 10
print("Powers of 2:", [2**x for x in range(n)])