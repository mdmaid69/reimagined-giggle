def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
def is_palindrome(s):
        return s == s[::-1]