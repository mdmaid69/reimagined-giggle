text = "Hello, world!"
print("Characters:", len(text))
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)