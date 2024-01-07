  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import random
def roll_die():
        return random.randint(1, 6)