  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)