import random
def roll_die():
        return random.randint(1, 6)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value