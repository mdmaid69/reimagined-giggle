import time
def get_current_time():
        return time.time()
def is_palindrome(s):
        return s == s[::-1]