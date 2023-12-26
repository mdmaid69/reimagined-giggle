  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"