n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])