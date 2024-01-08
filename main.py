  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)