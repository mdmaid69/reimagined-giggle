  import os
  def split_path(path):
        return os.path.split(path)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)