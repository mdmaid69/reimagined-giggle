  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))