import datetime
def get_today_date():
        return datetime.date.today()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])