  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)