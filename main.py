import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b