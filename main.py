import datetime
def get_today_date():
        return datetime.date.today()
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])