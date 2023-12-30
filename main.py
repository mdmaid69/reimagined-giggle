i = 0
while i < 5:
        print(i)
        i += 1
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])