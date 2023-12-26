  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  def remove_duplicates(lst):
        return list(set(lst))