import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)