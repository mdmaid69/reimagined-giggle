  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
def calculate_average(lst):
        return sum(lst) / len(lst)