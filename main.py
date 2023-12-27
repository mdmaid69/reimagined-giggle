import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)