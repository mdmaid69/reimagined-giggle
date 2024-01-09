  import os
  def get_base_name(path):
        return os.path.basename(path)
n = 10
print("Square numbers:", [x**2 for x in range(n)])