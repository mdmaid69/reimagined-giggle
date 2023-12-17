def calculate_energy(mass, c=3*10**8):
        return mass * c**2
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))