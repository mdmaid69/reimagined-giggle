n = 10
print("Square numbers:", [x**2 for x in range(n)])
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)