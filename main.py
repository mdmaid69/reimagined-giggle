def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
def is_palindrome(s):
        return s == s[::-1]