numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))