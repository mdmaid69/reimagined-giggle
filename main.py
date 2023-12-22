n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
def is_palindrome(s):
        return s == s[::-1]