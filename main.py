import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value