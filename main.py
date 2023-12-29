def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import datetime
def get_today_date():
        return datetime.date.today()