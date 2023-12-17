n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)