  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
def find_union(list1, list2):
        return set(list1) | set(list2)