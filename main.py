  import os
  def split_path(path):
        return os.path.split(path)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])