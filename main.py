import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)