  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])