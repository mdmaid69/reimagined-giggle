import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value