import random
def roll_die():
        return random.randint(1, 6)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"