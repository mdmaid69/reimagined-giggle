def calculate_force(mass, acceleration):
        return mass * acceleration
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))