  def square_number(x):
        return x**2
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)