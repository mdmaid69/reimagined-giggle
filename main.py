import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"