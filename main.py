  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))