  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])