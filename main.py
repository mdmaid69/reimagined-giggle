def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2