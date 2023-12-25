text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time