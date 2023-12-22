  import os
  def get_base_name(path):
        return os.path.basename(path)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])