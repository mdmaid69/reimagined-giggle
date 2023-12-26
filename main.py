import sys
def add_to_python_path(path):
        sys.path.append(path)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)