  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)