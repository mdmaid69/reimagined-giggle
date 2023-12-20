  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)