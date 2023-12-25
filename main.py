  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)