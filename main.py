import datetime
def get_today_date():
        return datetime.date.today()
def is_palindrome(s):
        return s == s[::-1]