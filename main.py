n = 10
print("Powers of 2:", [2**x for x in range(n)])
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))