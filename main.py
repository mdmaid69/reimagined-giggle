  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))