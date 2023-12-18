def calculate_energy(mass, c=3*10**8):
        return mass * c**2
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True