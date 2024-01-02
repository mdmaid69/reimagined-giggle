import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import datetime
def get_today_date():
        return datetime.date.today()