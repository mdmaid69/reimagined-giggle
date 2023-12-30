  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b