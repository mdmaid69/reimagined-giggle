  def convert_to_octal(n):
        return oct(n)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)