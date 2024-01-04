import datetime
def get_current_datetime():
        return datetime.datetime.now()
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)