n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
def is_palindrome(s):
        return s == s[::-1]