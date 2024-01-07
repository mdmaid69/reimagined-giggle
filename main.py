numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value