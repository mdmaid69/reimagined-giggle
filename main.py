  import sys
  def get_python_version():
        return sys.version
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))