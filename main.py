  import os
  def get_current_working_directory():
        return os.getcwd()
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])