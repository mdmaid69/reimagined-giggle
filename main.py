n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))