  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import math
def calculate_permutations(n, k):
        return math.perm(n, k)