def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()