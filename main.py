  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
n = 10
print("Cube numbers:", [x**3 for x in range(n)])