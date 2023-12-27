  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import sys
def add_to_python_path(path):
        sys.path.append(path)