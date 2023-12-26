import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"