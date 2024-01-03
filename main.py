n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
n = 10
print("Cube numbers:", [x**3 for x in range(n)])