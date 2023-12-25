import time
def get_current_time():
        return time.ctime()
def is_palindrome(s):
        return s == s[::-1]