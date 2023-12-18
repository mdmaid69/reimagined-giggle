  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))