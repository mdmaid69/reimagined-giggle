  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
n = 10
print("Cube numbers:", [x**3 for x in range(n)])