n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time