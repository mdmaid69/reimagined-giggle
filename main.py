  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])