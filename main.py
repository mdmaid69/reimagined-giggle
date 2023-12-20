import random
def generate_random_choice(choices):
        return random.choice(choices)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)