  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import datetime
def get_current_date():
        return datetime.date.today()