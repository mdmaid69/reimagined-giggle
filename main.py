n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)