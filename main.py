  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import random
def generate_random_sample(population, k):
        return random.sample(population, k)