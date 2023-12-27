n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)