n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import datetime
def get_current_datetime():
        return datetime.datetime.now()