  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])