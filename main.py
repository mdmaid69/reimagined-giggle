  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)