def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)