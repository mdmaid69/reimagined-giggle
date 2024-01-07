def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)