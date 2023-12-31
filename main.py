  import sys
  def get_python_version():
        return sys.version
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))