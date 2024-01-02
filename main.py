  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)