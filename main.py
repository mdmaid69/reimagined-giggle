import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import sys
  def get_python_version():
        return sys.version