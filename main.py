n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]