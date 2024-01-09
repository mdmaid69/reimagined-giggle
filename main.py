  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
n = 10
print("Square numbers:", [x**2 for x in range(n)])