n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)