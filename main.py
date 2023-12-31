n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)