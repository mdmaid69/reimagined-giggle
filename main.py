  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True
import random
def generate_random_sample(population, k):
        return random.sample(population, k)