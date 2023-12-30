  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2