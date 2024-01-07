n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)