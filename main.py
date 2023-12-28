import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])