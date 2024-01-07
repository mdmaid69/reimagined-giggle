n = 10
print("Cube numbers:", [x**3 for x in range(n)])
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)