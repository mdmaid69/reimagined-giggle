  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))