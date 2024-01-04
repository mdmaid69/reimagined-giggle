  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import itertools
print(list(itertools.permutations([1, 2, 3])))