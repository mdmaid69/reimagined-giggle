  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))