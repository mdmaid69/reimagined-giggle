import datetime
def get_today_date():
        return datetime.date.today()
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b