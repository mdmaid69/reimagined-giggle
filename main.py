  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])