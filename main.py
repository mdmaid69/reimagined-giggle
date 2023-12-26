  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)