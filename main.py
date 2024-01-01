def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def is_palindrome(s):
        return s == s[::-1]