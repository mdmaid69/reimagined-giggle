  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)