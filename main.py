  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])