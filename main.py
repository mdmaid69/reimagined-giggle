  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])