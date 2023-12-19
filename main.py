import random
print(random.randint(0, 100))
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b