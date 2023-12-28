  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value