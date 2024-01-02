import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height