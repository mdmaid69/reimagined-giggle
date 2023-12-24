  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"