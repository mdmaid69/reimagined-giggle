import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)