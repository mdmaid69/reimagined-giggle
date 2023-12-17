  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import random
def generate_random_number(start, end):
        return random.randint(start, end)