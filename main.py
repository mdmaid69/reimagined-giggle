import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"