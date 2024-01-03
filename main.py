import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value