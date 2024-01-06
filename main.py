  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"