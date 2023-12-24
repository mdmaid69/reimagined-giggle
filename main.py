  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)