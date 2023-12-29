import datetime
def get_today_date():
        return datetime.date.today()
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)