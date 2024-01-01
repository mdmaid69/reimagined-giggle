n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))