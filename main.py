  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])