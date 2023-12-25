import datetime
def get_today_date():
        return datetime.date.today()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])