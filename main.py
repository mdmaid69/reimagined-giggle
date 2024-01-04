  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)