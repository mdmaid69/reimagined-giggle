  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])