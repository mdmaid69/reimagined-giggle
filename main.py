import datetime
def get_current_datetime():
        return datetime.datetime.now()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)