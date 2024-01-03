import datetime
def get_current_datetime():
        return datetime.datetime.now()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)