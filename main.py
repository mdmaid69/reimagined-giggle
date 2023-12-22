  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time