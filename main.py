import datetime
def get_today_date():
        return datetime.date.today()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])