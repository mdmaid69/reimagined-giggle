import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)