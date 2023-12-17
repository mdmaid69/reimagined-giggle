import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)