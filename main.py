n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))