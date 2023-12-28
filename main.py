  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)