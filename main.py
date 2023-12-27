  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))