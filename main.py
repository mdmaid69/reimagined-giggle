import random
def generate_random_choice(choices):
        return random.choice(choices)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"