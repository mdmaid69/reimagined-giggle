import random
def roll_die():
        return random.randint(1, 6)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)