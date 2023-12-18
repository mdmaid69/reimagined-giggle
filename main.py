  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value