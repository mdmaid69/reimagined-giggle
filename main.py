  import os
  def delete_file(file_name):
        os.remove(file_name)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)