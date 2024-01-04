  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])