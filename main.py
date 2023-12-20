  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import datetime
def get_today_date():
        return datetime.date.today()