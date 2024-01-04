  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time