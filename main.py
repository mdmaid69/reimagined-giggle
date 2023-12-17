def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import json
print(json.dumps({"name": "John", "age": 30}))