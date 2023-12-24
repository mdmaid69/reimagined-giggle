  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time