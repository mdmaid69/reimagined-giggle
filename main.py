import datetime
def get_current_datetime():
        return datetime.datetime.now()
def is_palindrome(s):
        return s == s[::-1]