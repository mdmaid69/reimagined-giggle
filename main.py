def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
n = 10
print("Powers of 2:", [2**x for x in range(n)])