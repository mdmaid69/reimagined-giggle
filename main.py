  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))