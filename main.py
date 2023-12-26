import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days