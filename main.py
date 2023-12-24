  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)