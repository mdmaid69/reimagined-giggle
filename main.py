def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))