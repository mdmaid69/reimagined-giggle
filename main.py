import time
def get_time_since_epoch():
        return time.time()
def is_palindrome(s):
        return s == s[::-1]