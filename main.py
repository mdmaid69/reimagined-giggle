  import os
  def get_directory_name(path):
        return os.path.dirname(path)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])