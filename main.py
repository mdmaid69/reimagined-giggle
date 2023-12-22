def is_palindrome(s):
        return s == s[::-1]
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time