def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)