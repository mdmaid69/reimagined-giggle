def is_palindrome(s):
        return s == s[::-1]
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])