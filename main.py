import datetime
def get_today_date():
        return datetime.date.today()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)