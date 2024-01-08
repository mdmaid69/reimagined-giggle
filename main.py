  def is_even(n):
        return n % 2 == 0
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)