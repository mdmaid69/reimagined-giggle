def is_palindrome(s):
        return s == s[::-1]
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time