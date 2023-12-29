  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)