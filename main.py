import re
print(re.match("h.*o", "hello world"))
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)