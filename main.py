import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"