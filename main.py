  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)