n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)