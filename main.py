def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())