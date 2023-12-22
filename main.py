def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"