import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days