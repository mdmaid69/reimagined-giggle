import datetime
def get_current_datetime():
        return datetime.datetime.now()
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])