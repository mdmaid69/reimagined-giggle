import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)