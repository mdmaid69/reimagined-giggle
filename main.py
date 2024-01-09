  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])