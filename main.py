n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import re
print(re.match("h.*o", "hello world"))