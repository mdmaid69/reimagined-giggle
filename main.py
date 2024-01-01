import re
print(re.match("h.*o", "hello world"))
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)