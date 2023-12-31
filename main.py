  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)