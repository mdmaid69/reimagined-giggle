import os
def get_environment_variable(var):
        return os.getenv(var)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"