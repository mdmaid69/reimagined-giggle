def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)