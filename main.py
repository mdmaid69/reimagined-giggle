n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])