import os
def change_working_directory(path):
        os.chdir(path)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)