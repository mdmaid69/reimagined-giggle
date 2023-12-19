n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
def calculate_energy(mass, c=3*10**8):
        return mass * c**2