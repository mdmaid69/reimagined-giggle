  import os
  def get_directory_name(path):
        return os.path.dirname(path)
n = 10
print("Powers of 2:", [2**x for x in range(n)])