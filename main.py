  import os
  def get_base_name(path):
        return os.path.basename(path)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)