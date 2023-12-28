n = 10
print("Cube numbers:", [x**3 for x in range(n)])
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino