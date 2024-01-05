  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])