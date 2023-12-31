  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import os
def change_working_directory(path):
        os.chdir(path)