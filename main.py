  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)