import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)