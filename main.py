  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
n = 10
print("Square numbers:", [x**2 for x in range(n)])