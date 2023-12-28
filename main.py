  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
n = 10
print("Square numbers:", [x**2 for x in range(n)])