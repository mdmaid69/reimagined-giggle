  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)