  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)