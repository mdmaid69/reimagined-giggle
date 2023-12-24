  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)