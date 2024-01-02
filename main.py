text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)