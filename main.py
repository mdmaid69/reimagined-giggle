  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])