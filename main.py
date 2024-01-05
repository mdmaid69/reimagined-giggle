import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)