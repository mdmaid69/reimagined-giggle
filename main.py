  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)