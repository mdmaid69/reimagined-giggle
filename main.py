import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)