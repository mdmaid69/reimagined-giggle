  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
def remove_duplicates(lst):
        return list(set(lst))