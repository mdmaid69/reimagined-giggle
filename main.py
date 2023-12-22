  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"