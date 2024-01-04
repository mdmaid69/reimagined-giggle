text = "Hello, world!"
print("Uppercase:", text.upper())
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)