def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def greet(name):
        print(f"Hello, {name}!")