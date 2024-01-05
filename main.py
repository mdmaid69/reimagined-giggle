  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"