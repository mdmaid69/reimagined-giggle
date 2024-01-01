  import os
  def get_base_name(path):
        return os.path.basename(path)
n = 10
print("Powers of 2:", [2**x for x in range(n)])