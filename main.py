import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)