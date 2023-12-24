  import os
  def delete_file(file_name):
        os.remove(file_name)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])