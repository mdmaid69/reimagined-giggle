import datetime
def get_today_date():
        return datetime.date.today()
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)