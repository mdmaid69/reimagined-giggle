def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])