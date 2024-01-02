  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])