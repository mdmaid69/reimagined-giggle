def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])