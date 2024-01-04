import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)