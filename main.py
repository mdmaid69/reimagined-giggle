  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)