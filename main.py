  import os
  def split_path(path):
        return os.path.split(path)
n = 10
print("Powers of 2:", [2**x for x in range(n)])