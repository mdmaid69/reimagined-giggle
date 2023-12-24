  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])