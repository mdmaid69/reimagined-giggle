n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
def calculate_energy(mass, c=3*10**8):
        return mass * c**2