n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
from collections import Counter
print(Counter("hello world"))