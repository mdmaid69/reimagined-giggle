import datetime
def get_current_datetime():
        return datetime.datetime.now()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])