import datetime
def get_today_date():
        return datetime.date.today()
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])