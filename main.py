import time
def get_current_time():
        return time.time()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)