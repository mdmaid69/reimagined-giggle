  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"