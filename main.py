numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)