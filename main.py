n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b