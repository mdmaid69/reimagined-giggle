  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"