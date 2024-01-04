n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])