import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)