  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time