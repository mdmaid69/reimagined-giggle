  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
def find_union(list1, list2):
        return set(list1) | set(list2)