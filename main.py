  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)