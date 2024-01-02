  import os
  def get_directory_name(path):
        return os.path.dirname(path)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])